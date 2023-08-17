from django.http import HttpResponse,response


def not_found_view(request, *args, **kwargs):
    response.status_code = 404
    default_image_path = "staticfiles/images/error_404.png"
    with open(default_image_path, "rb") as default_image_file:
        default_image_data = default_image_file.read()

    current_response = HttpResponse(default_image_data, content_type='image/png', status=404)
    return current_response


def server_error_view(request, *args, **kwargs):
    response.status_code = 500
    default_image_path = "staticfiles/images/error_404.png"
    with open(default_image_path, "rb") as default_image_file:
        default_image_data = default_image_file.read()

    current_response = HttpResponse(default_image_data, content_type='image/png', status=500)
    return current_response


def forbidden_view(request, *args, **kwargs):
    response.status_code = 403
    default_image_path = "staticfiles/images/forbidden.png"
    with open(default_image_path, "rb") as default_image_file:
        default_image_data = default_image_file.read()

    current_response = HttpResponse(default_image_data, content_type='image/png', status=403)
    return current_response


