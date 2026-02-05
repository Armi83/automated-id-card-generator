from PIL import Image,ImageFont,ImageDraw
import pandas as pd
import os

df=pd.read_excel("E:\\college\\other\\python\\ID_Card\\sample.xlsx",sheet_name="Harry Potter")

for i,row in df.iterrows():

    img=Image.open("E:\\college\\other\\python\\ID_Card\\ID.png")
    draw=ImageDraw.Draw(img)

    photo_path=f"E:\\college\\other\\python\\ID_Card\\Photo\\{row["PHOTO"]}"
    if os.path.exists(photo_path):
        photo=Image.open(photo_path).resize((293,405),Image.Resampling.LANCZOS)
        img.paste(photo,(85,138))
    else:
        print("Not Found Photo : ",row["NAME"])

    font=ImageFont.truetype("arialbd.ttf",47)
    draw.text((558,212),row["NAME"],fill="Black",font=font)

    font=ImageFont.truetype("arialbd.ttf",28)
    draw.text((503,280),str(row["STD"]),fill="Black",font=font)

    font=ImageFont.truetype("arial.ttf",23)

    birthdate=row["BIRTH DATE"]
    bdate=birthdate.strftime("%d-%m-%Y") if pd.notna(birthdate) else " "
    draw.text((433,420),bdate,fill="Black",font=font)
    draw.text((666,420),str(row["UID NUMBER"]),fill="Black",font=font)
    draw.text((666,494),str(row["ADDRESS"]),fill="Black",font=font)
    draw.text((433,494),str(row["MOBILE NUMBER"]),fill="Black",font=font)

    output_path=f"E:\\college\\other\\python\\ID_Card\\{row["NAME"]}_ID.png"
    img.save(output_path)