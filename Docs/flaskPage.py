from flask import Flask, redirect, render_template, request

app = Flask(__name__)

# Dictionary mapping chapter numbers to Google Drive links
chapter_links = {
    '01': "https://drive.google.com/file/d/1xNcJvgbgqWYWCx88DmKpqWPQZl0Lg57q/view?usp=share_link",
    '02': "https://drive.google.com/file/d/1AJPhu7BKiulVZYt4dZhfln-K1-IRIG0B/view?usp=share_link",
    '03': "https://drive.google.com/file/d/1n3Rn2gGRYIuQvSXDx4I1SOrxGnS4Jl4d/view?usp=share_link",
    '04': "https://drive.google.com/file/d/1YNBvkcfpnL7juehPQtlqr18U28EgPkOY/view?usp=share_link",
    '05': "https://drive.google.com/file/d/1PKj54KOFtn9oKFSvEYiFSx0JSpjZyKyz/view?usp=share_link",
    '06': "https://drive.google.com/file/d/1VWlYaxJ5uOmXZKB5fvmZ7xMeT8GuNRvr/view?usp=share_link",
    '07': "https://drive.google.com/file/d/1ypP3RmXXShRIJcQ83g0LAUQy0zwRdgTs/view?usp=share_link",
    '08': "https://drive.google.com/file/d/19jl6Xknr8ciBOyhHkm0Ceh1W1j9y3UAw/view?usp=share_link",
    '09': "https://drive.google.com/file/d/1LU3A3U3aaoCSh0u_deCI-7PSUcCGMvgz/view?usp=share_link",
    '10': "https://drive.google.com/file/d/10R0BC56O7KYeZnI1WNW2RgN3QJjhjCdd/view?usp=share_link",
    '11': "https://drive.google.com/file/d/1wq80x-WPSrO3q1ZbjNkNndPxuNIsbAB5/view?usp=share_link",
    '12': "https://drive.google.com/file/d/1Mk0W5QedhiG30oHp8HUU6qbD3Sk6nxi-/view?usp=share_link",
    '13': "https://drive.google.com/file/d/1mIa0rTy1i8Yl9fqUhVDPpJiL1iJTuVjZ/view?usp=share_link",
    '14': "https://drive.google.com/file/d/1_Q_CTcZZkbtE-Zok4yPeLnGEp1_U5Q0Z/view?usp=share_link",
    '15': "https://drive.google.com/file/d/1W-5Xd4smUH_JJ8YtuPL77aG8SnqvXXju/view?usp=share_link",
    '16': "https://drive.google.com/file/d/1W-5Xd4smUH_JJ8YtuPL77aG8SnqvXXju/view?usp=share_link",
    '17': "https://drive.google.com/file/d/1ChrSsuYQIi_xneuOSDVQ2KqasDOKvDh4/view?usp=share_link",
    '18': "https://drive.google.com/file/d/1RL8ngAW9hl0u858RH2Z8iFx8jh8p_6rY/view?usp=share_link",
    '19': "https://drive.google.com/file/d/10wY6Mg_i0uyhrBL_CJd3tAzI2lw17618/view?usp=share_link",
    '20': "https://drive.google.com/file/d/1sG-UqWJw4MKp56VWDnhtMi-B9MFm4cc7/view?usp=share_link",
    '21': "https://drive.google.com/file/d/1LUUsWQBr8Z3aMuswPgAKdu1aOt6tun-C/view?usp=share_link",
    '22': "https://drive.google.com/file/d/1Zt4uitrtJd9QpZUIaQQpZu0lUe3aes4v/view?usp=share_link",
    '23': "https://drive.google.com/file/d/1MN-CVgwoSBrewPTXh_Byla1ZtbZwxPG7/view?usp=share_link",
    '24': "https://drive.google.com/file/d/1sG9QiI2dkjJB3UElOp4jUy926PzXFn2J/view?usp=share_link"
    
    # Add more chapters as needed
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/watch', methods=['GET', 'POST'])
def watch_jujutsu_kaisen_chapter():
    if request.method == 'POST':
        chapter = request.form['chapter']
        if chapter in chapter_links:
            chapter_link = chapter_links[chapter]
            return redirect(chapter_link)
        else:
            return "Chapter not found"
    else:
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
