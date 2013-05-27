from django.shortcuts import render
from encoders import Encoder

import models
import time
import sys,os


def home(request):
    message = None
    if request.method == "POST":
        print "POST parameters: ", request.POST
        print "Files: ", request.FILES

        # Build the form
        form = models.UploadModelForm(request.POST, request.FILES)

        if form.is_valid():
            # Read the data and upload it to the location defined in UploadModel
            form.save()

            # Save the name of the uploaded file
            uploaded_filename = form.cleaned_data['filepicker_file'].name

            # Build the full input path to the file
            MEDIA_UPLOAD_ROOT = os.path.join(os.getcwd(),'media/uploads/')
            input_path = MEDIA_UPLOAD_ROOT + uploaded_filename

            # Build the output filename
            output_filename = uploaded_filename + "_transcoded.mkv"

            # Build the output path
            MEDIA_DOWNLOADS_ROOT = os.path.join(os.getcwd(),'media/finished/')
            output_path = MEDIA_DOWNLOADS_ROOT + output_filename

            # Transcode the file
            video_encoder = Encoder(input_path, output_path)
            video_encoder.start()
            while video_encoder.alive():
                print(video_encoder.get_time_elapsed())
                time.sleep(0.1)

            # Return the path to the file
            message = output_filename
        else:
            message = None
    else:
        form = models.UploadModelForm()

    return render(request, "home.html", {'form': form, 'message': message})

