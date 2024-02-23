import io
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('AGG')


def visualise(data: list):
    event_ts_list = [data.get('event_ts') for data in data]
    qty_list = [data.get('qty') for data in data]
    plt.rcParams['figure.figsize'] = [20, 10]
    plt.rcParams['figure.autolayout'] = True
    plt.bar(event_ts_list, qty_list)
    img_buf = io.BytesIO()

    plt.xlabel("Periods")
    plt.ylabel("Quantity of events")
    plt.title("Quantity of events per dates")

    plt.savefig(img_buf, format='png')
    plt.close()
    return img_buf
