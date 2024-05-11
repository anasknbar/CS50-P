
    # base_image = Image.open(f"{path[1]}")

    # # crop the base image
    # width, height = base_image.size
    # # Calculate the coordinates for cropping
    # left = 0  # Left edge of the image (no cropping)
    # upper = 0  # Upper edge of the image (no cropping)
    # right = width  # Right edge of the image (no cropping)
    # lower = height - 200  # Crop 30 pixels from the bottom
    # # Crop the image using the specified coordinates
    # im_crop = base_image.crop((left, upper, right, lower))


    # # ---------------------------------------------------------
    # overlay_image = Image.open("shirt.png")
    # (width, height) = (overlay_image.width * 2, overlay_image.height * 2 )
    # im_resized = overlay_image.resize((width, height))

    # # ---------------------------------------------------------
    # position = (
    #     (im_crop.width - im_resized.width) // 2,
    #     # (im_crop.height - im_resized.height) // 2
    #     200
    # )

    # # Paste the overlay image onto the base image at the calculated position
    # im_crop.paste(im_resized, position, im_resized)

    # # Save the resulting image
    # im_crop.save(f"{path[2]}")
# main()

# Open the input image
input_image = Image.open("before1.jpg")
width,height = input_image.size 

    # Specify the target dimensions for resizing
target_size = (width, height-400)  # width, height

    # Resize and crop the image to fit within the target size
resized_image = ImageOps.fit(input_image, target_size)

    
overlay_image = Image.open("shirt.png")
(width, height) = (overlay_image.width * 2, overlay_image.height * 2 )

width,height = overlay_image.size
target_size = (width, height-400)
resized_image = ImageOps.fit(input_image, target_size)
resized_image.save("resized_image.jpg")