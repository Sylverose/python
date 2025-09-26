import os
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.backends.backend_pdf import PdfPages


file_path = os.path.join("data", "DKHousingPricesSample100k.csv")


# Set up custom font for all plots
font_path = os.path.join("fonts", "DanskeTextv2-Regular.ttf")
print(f"Resolved font path: {os.path.abspath(font_path)}")
print(f"Font file exists: {os.path.exists(font_path)}")
print(f"Current working directory: {os.getcwd()}")
prop = fm.FontProperties(fname=font_path)

try:
    if not os.path.exists(file_path):
        print(f"Filen blev ikke fundet: {file_path}")
    else:
        df = pd.read_csv(file_path)
        # Group by 'region' and 'house_type' and print the first 10 entries for each region
        grouped = df.groupby(['region', 'house_type']).apply(lambda x: x.head(10)).reset_index(drop=True)
        print("Første 10 indgange for hver region og hus type:")
        print(grouped)

        # Ensure directories exist before saving files
        os.makedirs(os.path.join("data", "csv_log"), exist_ok=True)
        os.makedirs(os.path.join("data", "csv_log", "housing_statistics"), exist_ok=True)

        # Save grouped data
        grouped.to_csv(os.path.join("data", "csv_log", "housing.csv"), index=False)

        # Purchases average purchases per region
        avg_purchases_per_region = df.groupby('region')[
            'purchase_price'].mean()
        print(f"Gennemsnitlige køb per region:\n{avg_purchases_per_region}")

        # Save average purchases per region to file
        avg_purchases_per_region.to_csv(
            os.path.join("data", "csv_log", "housing_statistics", "average_purchase.txt"),
            header=["average_purchase"]
        )

        # Plot the graph of average purchases per region (smaller size)
        fig, ax = plt.subplots(figsize=(6, 3))
        avg_purchases_per_region.plot(
            kind='bar',
            title='Gennemsnitlige køb per region',
            ylabel='Gennemsnitlige køb',
            xlabel='Region',
            color='#003778',
            ax=ax
        )
        ax.set_title('Gennemsnitlige køb per region', fontproperties=prop)
        ax.set_xlabel('Region', fontproperties=prop)
        ax.set_ylabel('Gennemsnitlige køb', fontproperties=prop)
        # Set font for tick labels
        for label in ax.get_xticklabels() + ax.get_yticklabels():
            label.set_fontproperties(prop)
        plt.tight_layout()
        plt.show()

        # Save the plot and statistics to a single PDF page, with text directly under the graph (portrait orientation)
        pdf_path = os.path.join(
            "data", "csv_log", "housing_statistics", "average_purchase_per_region.pdf")
        with PdfPages(pdf_path) as pdf:
            # Portrait orientation: taller than wide
            fig, (ax1, ax2) = plt.subplots(
                2, 1, figsize=(6, 9), gridspec_kw={'height_ratios': [2, 1]})
            # Bar chart
            avg_purchases_per_region.plot(
                kind='bar',
                title='Gennemsnitlige køb per region',
                ylabel='Gennemsnitlige køb',
                xlabel='Region',
                color='#003778',
                ax=ax1
            )
            ax1.set_title('Gennemsnitlige køb per region', fontproperties=prop)
            ax1.set_xlabel(
                'Gennemsnitlige værdier i DKK, fordelt på regioner', fontproperties=prop)
            ax1.set_ylabel('Gennemsnitlige køb', fontproperties=prop)
            for label in ax1.get_xticklabels() + ax1.get_yticklabels():
                label.set_fontproperties(prop)
            # Print the name of each region and corresponding average purchase below the chart and align left
            for i, (region, avg) in enumerate(avg_purchases_per_region.items()):
                ax2.text(0.01, 0.95 - i * 0.05, f"{region}: {avg:.2f}",
                         fontsize=10, fontproperties=prop, va='top', ha='left')
            # Turn off axis
            ax2.axis('off')
            # Add today's date to the top right corner
            today_str = datetime.now().strftime('Dato:'+'%d-%m-%Y')
            fig.text(0.98, 0.98, today_str, ha='right',
                     va='top', fontsize=10, fontproperties=prop)
            plt.tight_layout()  # Restore tight_layout for PDF
            pdf.savefig(fig)
            plt.close(fig)

            # Donut chart: number of bonds per region
            bonds_per_region = df.groupby('region')['yield_on_mortgage_credit_bonds%'].count()
            fig3, ax3 = plt.subplots(figsize=(6, 6))
            custom_colors = [
                "#007bc8", "#ec9896", "#c7ddeb", "#e5dfcf",
                "#FFB300", "#E15759", "#76B7B2", "#59A14F"
            ]
            wedges, texts, autotexts = ax3.pie(
                bonds_per_region,
                labels=bonds_per_region.index,
                autopct='%1.1f%%',
                startangle=90,
                pctdistance=0.85,
                colors=custom_colors[:len(bonds_per_region)],
                textprops={'fontproperties': prop}
            )
            # Draw a white circle in the center to make it a donut
            centre_circle = plt.Circle((0, 0), 0.6, fc='white')
            fig3.gca().add_artist(centre_circle)
            ax3.set_title('Obligationer pr. region', fontproperties=prop)
            # Set font for labels
            for text in texts + autotexts:
                text.set_fontproperties(prop)
            # Add today's date to the top right corner
            fig3.text(0.98, 0.98, today_str, ha='right',
                      va='top', fontsize=10, fontproperties=prop)
            plt.tight_layout()  # Restore tight_layout for PDF
            pdf.savefig(fig3)
            plt.close(fig3)
except FileNotFoundError:
    print(f"Kunne ikke finde filen: {file_path}")
except PermissionError:
    print(f"Adgang nægtet ved læsning af: {file_path}")
except Exception as e:
    print(f"Der opstod en fejl: {e}")

