from utils.visualizer import visualise


def create_response(data, start_date, end_date, **kwargs):
    if data:

        response = visualise(data=data, **kwargs)

        headers = {'Content-Disposition': 'inline; filename="out.png"'}
        media_type = 'image/png'
        code = 200
    else:
        response = f"<html>No data found for period: {start_date} - {end_date}</html>"
        headers = None
        media_type = 'text/html'
        code = 404
    return response, headers, media_type, code
