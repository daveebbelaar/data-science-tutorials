import matplotlib.pyplot as plt
import datetime
import os


class Figure:
    def export_figure(self, filename):

        # Change filename to avoid potenial errors when exporting with "/"
        filename = filename.replace("/", "-")

        date = datetime.date.today().strftime("%d-%m-%Y")
        path = f"../../reports/figures/{date}/"

        if os.path.exists(path):
            plt.savefig(path + str(filename) + ".png", bbox_inches="tight")

        if not os.path.exists(path):
            os.makedirs(path)
            plt.savefig(path + str(filename) + ".png", bbox_inches="tight")

        print(f"Successfully export {str(filename)}")
