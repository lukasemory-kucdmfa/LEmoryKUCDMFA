import os

# Specify the directory where you want to save the text files
directory = "txt_files"

# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

# Predefined content for each of the 24 files
content = [
    "The purple button that says 'Authorize' is a good use of a focal color for a primary call to action. There is appropiate padding in text boxes and good contrast for the text and the background.",
    "The thumbnail for the video is the top of heirarchy. The text 'Keep it Natural' on the image is good but the other text on the image is too small. There is a good use of a red notifcation badge in the bottom menu.",
    "The design of this interface prioritizes the brand of the images instead of the app itself. It could be better if the PlayStation brand was more prominent with a logo or more obvious focal color.",
    "The image in the header is too busy and makes the components on top of it difficult to focus on. There are also too many options for navigation instead of one or two primary methods.",
    "There is a good use of the focal color for the brand. The thumbnail for the video does not distract from the components on top of it.",
    "There are two good uses of the red noification badge. The design is organized and easy to read with appropriate margins and padding. The use of darkening colors in the progress bars tell the user information without using text.",
    "There is a consistent use of rounded rectangles and subtle layering and drop shadows to give dimension to the design. Text is good size and color contrastt is good.",
    "For a loading screen, this successfully uses text to tell the story of the brand and limits the palette to a few on-brand colors.",
    "There are design motifs that make the brand feel more approachable. But there is a lot going on with badges, focal colors, and multiple calls to action which can be overwhelming. There is text that says the name of the user, in this case 'Lukas' which makes the brand feel more approachable, too.",
    "This is a good use of telling the user what you want them to do by recommending specific content to look at and click on. There is a black overlay on less important content so we focus on the most important content.",
    "There is text that says the name of the user, in this case 'Lukas' which makes the brand feel more approachable. There is a prominent use of the primary brand colors so the user feels immersed. Big text that says 'Deal of the Day' acts as a recommendation for what the developer wants the user to interact with.",
    "There is a clear hierarchy of image, album name, song names, and artist name. There is a successful combination of the primary brand color green for the call to action and the purple color of the partnership brand.",
    "There is a good green focal color that isn't used anywhere else in the brand. The most important information—the product image and the price—are the highest part of the heirarchy which is good. There is a good red notification badge.",
    "There is a smart use of greyed out content which would encourage the user to engage with the app to unlock it. However, the text is too small and the color contrast is too low in the call to action 'Unlock all games and levels'. There is a good organization of content with consistent navigation styles.",
    "This is a good example of a popup that darkens the original content and draws the user's attention to the popup. There is a clear design system for the multiple choice so you can tell which option you've chosen based on both color and shape.",
    "There is a clear hierarchy of image, album name, song names, and artist name. There is a successful combination of the primary brand color green for the call to action and the maroon color of the partnership brand. There is very strong contrast for the components and the background.",
    "This is a good example of a popup that darkens the original content and draws the user's attention to the popup. While the icons are all appropriately spaced and sized, they are hard to read through because they are not in a clear order. They are not alphabetical or easy to sort or search through. They are not categorized which makes it hard to find the tool you want.",
    "This is a good example of a login screen because it gives user the option to sign it with Google, Apple, or Facebook. There is a clear primary call to action with the dark 'Continue' button and secondary buttons for Google, Facebook, and Apple. There is a focal color so you can tell which content you are interacting with.",
    "There are well designed toggles that change color and contrast so you can tell which ones have been interacted with. There is a clear call to action with the blue 'Live View' button. The secondary actions are well organized into rounded squares and there is a red notifcation badge that says 'NEW' to draw attention to new features.",
    "This is not the best example of a login screen because it doesn't give the user the option to sign in with Google, Apple, or Facebook. It only lets you login with your ID or Face ID and does not let you sign up right away. There are four dots that look like they would represent navigation or a carousel but they do not have any functionality—a different design system would be better.",
    "This design is well organized with correct padding and margins, but there is no mention of the brand anywhere. The color palette and fonts are on brand, but there should be a logo or a mention of the brand somewhere.",
    "This is a good example of a navigation page. It does incorporate visuals to compliment the text in the menu so it is not just a wall of text. There is consistent padding and font sizes so it is easy to read. There is no mention of the brand anywhere, not even in color or font.",
    "There is a consistent use of rounded rectangles and subtle layering and drop shadows to give dimension to the design. Text is good size and color contrastt is good. There is a very clear heirarchy for font sizes so the headlines 'Profile & Settings', 'Security', and 'Help Center' are easy to quickly find. There is text that says the name of the user, in this case 'Lukas' which makes the brand feel more approachable." ,
    "This is a nice example of a character customization page. You can navigate through body parts, colors, and styles in three different places so you can dynamically create your character. The biggest part of the heirarchy is your character so you can see the changes happen in real time. There is a focal color in the call to action 'Save' so you remember the brand.",
]

# Create 24 text files with specific content
for i in range(1, 25):
    file_name = f"text_file_{i}.txt"
    file_path = os.path.join(directory, file_name)
    
    # Write predefined content into each file
    with open(file_path, 'w') as file:
        file.write(content[i - 1])  # Write the specific content for each file
    
    print(f"Created: {file_path} with content: {content[i - 1]}")