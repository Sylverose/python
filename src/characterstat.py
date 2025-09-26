# characterstat.py - Python assignment part 1
import os
from collections import Counter
import matplotlib.pyplot as plt
import wordcloud as wc
from matplotlib.backends.backend_pdf import PdfPages

# Use raw string or forward slashes for cross-platform compatibility
file_path = r"data\Navneliste.txt"

try:
    # Check if the file exists before opening
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
    else:
        with open(file_path, "r", encoding="utf-8") as f:
            # Read all names, remove empty lines, and sort alphabetically
            names = [line.strip() for line in f if line.strip()]

            # Remove commas and sort alphabetically
            names = [name.replace(',', '') for name in names]
            names_sorted = sorted(names, key=lambda name: (len(name), name))

            # Ensure the output directory exists
            os.makedirs(os.path.join("data", "names"), exist_ok=True)

            # Print a sorted name list in data/names/sorted_names.txt where words are displayed one per line
            with open(os.path.join("data", "names", "sorted_names.txt"), "w", encoding="utf-8") as sorted_file:
                for name in names_sorted:
                    sorted_file.write(name + "\n")

            print("Sorterede navne:")
            for name in names_sorted:
                print(name)
            total_chars = sum(len(name) for name in names_sorted)
            print(f"\nAntal tegn i listen: {total_chars}")

            # Count how many times each character is used (case-insensitive)
            all_chars = ''.join(names_sorted).lower()
            char_counts = Counter(all_chars)
            print("\nAntal af hver tegn:")
            for char, count in sorted(char_counts.items()):
                print(f"'{char}': {count}")

            # Visualize as a bar chart (text-based)
            print("\nSøjlediagram over tegnfrekvens:")
            for char, count in sorted(char_counts.items()):
                bar = '█' * count
                print(f"{char}: {bar} ({count})")

            # Use matplotlib to create a graphical bar chart for the character frequencies
            chars, counts = zip(*sorted(char_counts.items()))  # Unzip into two lists for plotting
            fig1 = plt.figure()
            plt.bar(chars, counts, color='#003778')  # Dark blue color for bars
            plt.title('Tegnfrekvens i navnelisten')  # Title
            plt.xlabel('Tegn')  # X-axis label
            plt.ylabel('Frekvens')  # Y-axis label
            plt.tight_layout()
            plt.show()

            # Generate and display a word cloud of character frequencies
            wordcloud = wc.WordCloud(
                width=800, height=400, background_color='white'
            ).generate_from_frequencies(char_counts)
            fig2 = plt.figure(figsize=(10, 5))
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis('off')  # Hide axes
            plt.tight_layout()
            plt.show()

            # Save both charts to a single PDF
            pdf_path = os.path.join("data", "names", "character_stats.pdf")
            with PdfPages(pdf_path) as pdf:
                # Bar chart
                plt.figure(fig1.number)
                pdf.savefig(fig1)
                # Word cloud
                plt.figure(fig2.number)
                pdf.savefig(fig2)
        print(f"\nFilen blev behandlet og navne sorteret!")

except FileNotFoundError:
    print(f"Kunne ikke finde filen: {file_path}")
except PermissionError:
    print(f"Adgang nægtet ved læsning af: {file_path}")
except Exception as e:
    print(f"Der opstod en fejl: {e}")