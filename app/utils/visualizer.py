import io

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('AGG')


def visualise(data: list, x_label: str, y_label: str, title: str, x_axes_values: str, y_axes_values: str):

    x_axes = [data.get(x_axes_values).strftime("%Y-%m-%d %H:%M") for data in data]
    y_axes = [data.get(y_axes_values) for data in data]
    plt.rcParams['figure.figsize'] = [20, 10]
    plt.rcParams['figure.autolayout'] = True

    plt.bar(x_axes, y_axes, width=0.4)

    img_buf = io.BytesIO()

    plt.gcf().autofmt_xdate()
    plt.xticks(rotation=70)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)

    plt.savefig(img_buf, format='png')
    plt.close()
    return img_buf.getvalue()
