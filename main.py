import aspose.pdf as pdf

# Load the license
license = pdf.License()
license.set_license("Aspose.Total.lic")

# Load input PDF document
document = pdf.Document("Combine.pdf")

# Set watermark image
stamp = pdf.ImageStamp("Sample.jpg")

# Set properties for the watermark
stamp.x_indent = 200
stamp.y_indent = 200
stamp.height = 60
stamp.width = 60
stamp.background = True

# Add watermark image
document.pages[1].add_stamp(stamp)

# Save the PDF with watermark
document.save("Watermark.pdf")

print("Watermark added successfully")
