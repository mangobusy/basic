import base64
with open("C:\\Users\\admin\\Desktop\\大学资料\\学习\\概率论与数理统计\\homework2\\微信图片_20220924142058.jpg",'rb') as f:
    base64_data = base64.b64encode(f.read())
    s = base64_data.decode()
    print(s)
