import io

import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('AGG')


def visualise(data: list, x_label: str, y_label: str, title: str):

    event_ts_list = [data.get('events_date') for data in data]
    qty_list = [data.get('qty') for data in data]
    plt.rcParams['figure.figsize'] = [20, 10]
    plt.rcParams['figure.autolayout'] = True

    plt.bar(event_ts_list, qty_list, width=0.4)

    img_buf = io.BytesIO()

    plt.xticks(rotation=90)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)

    plt.savefig(img_buf, format='png')
    plt.close()
    return img_buf.getvalue()
