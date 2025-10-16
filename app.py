from flask import Flask, render_template, request, redirect, url_for

# 初始化 Flask 應用程式
app = Flask(__name__)

# 使用一個簡單的 Python 列表來模擬資料庫
posts = [
    {
        'id': 1,
        'author': '張三',
        'title': '第一篇文章',
        'content': '這是我的第一篇部落格文章，歡迎大家！'
    },
    {
        'id': 2,
        'author': '李四',
        'title': 'Flask 學習心得',
        'content': 'Flask 是一個輕量級且強大的 Python 網站框架。'
    }
]
# 用於生成新文章 ID
next_id = 3

# 網站首頁：顯示所有文章列表
@app.route('/')
def index():
    return render_template('index.html', posts=posts)

# 顯示單篇文章內容
@app.route('/post/<int:post_id>')
def post(post_id):
    # 根據 post_id 尋找對應的文章
    post = next((post for post in posts if post['id'] == post_id), None)
    if post:
        return render_template('post.html', post=post)
    return '文章不存在', 404

# 建立新文章
@app.route('/create', methods=('GET', 'POST'))
def create():
    global next_id
    if request.method == 'POST':
        # 從表單獲取資料
        title = request.form['title']
        author = request.form['author']
        content = request.form['content']

        # 簡單的驗證
        if not title or not author or not content:
            # 可以在此處添加錯誤訊息提示
            return render_template('create.html', error='所有欄位都是必填的！')

        # 建立新文章並添加到列表中
        new_post = {
            'id': next_id,
            'author': author,
            'title': title,
            'content': content
        }
        posts.append(new_post)
        next_id += 1
        
        # 重新導向到首頁
        return redirect(url_for('index'))

    # 如果是 GET 請求，就顯示建立文章的表單
    return render_template('create.html')

if __name__ == '__main__':
    # 啟動 Flask 應用程式，並開啟除錯模式
    app.run(debug=True)
