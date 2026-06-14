current_playlist = []

while True:
    print("""
    ======== HỆ THỐNG QUẢN LÝ PLAYLIST SPORTIFY ========
    1. Thêm bài hát mới & phân tích dữ liệu
    2. Quản lý danh sách phát
    3. Tìm kiếm và thay thế bài hát
    4. Sắp xếp danh sách phát
    5. Thoát chương trình
    =====================================================
          """)
    choice = input("Vui lòng chọn một tùy chọn (1-5): ")

    match choice:
        case "1":
            song_title = (input("Tên bài hát: "))
            title = song_title.strip().title()

            art = artist_name = str(input("Tác giả: "))
            art.strip().upper()

            genres_string = input("Thể loại: ")
            list=genres_string.split(",")

            newtitle = input("nhập tên bài hát mới: ")
            newart = input("nhập tên tác giả mới: ")

            new_song = {
            "Tên bài hát mới ": newtitle,
            "Tên tác giả mới ": newart,
            }

            current_playlist.append(new_song)


            print(title)
            print(art)
            print(current_playlist)
            
        case "2":
            print("Bạn đã chọn: Quản lý danh sách phát")
           
        case "3":
            print("Bạn đã chọn: Tìm kiếm và thay thế bài hát")
          
        case "4":
            print("Bạn đã chọn: Sắp xếp danh sách phát")
     
        case "5":
            print("Thoát chương trình. Hẹn gặp lại!")
            break
        case _:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")