1. Создать пост:
  - метод "POST"
  - URL: http://127.0.0.1:5000/posts
  - запросы:
    {            
    	"post_id": 1,
    	"title": "First article",
    	"body": "Hello!",
    	"author": "Me"
    },
    {
    	"post_id": 2,
    	"title": "Second article",
    	"body": "Hello again!",
    	"author": "Me"
    }

2. Вывести посты:
   - метод "GET"
   - URL: http://127.0.0.1:5000/posts

3. Вывести пост с id: 2:
   - метод "GET"
   - URL: http://127.0.0.1:5000/posts/2

4. Изменить пост с id: 2:
   - метод "PUT"
   - URL: http://127.0.0.1:5000/posts/2
   - запрос:
     {
    	"post_id": 2,
    	"title": "Second article CHANGED",
    	"body": "Hello again CHANGED!",
    	"author": "Me"
    }

5. Изменить пост с id: 1:
   - метод "DELETE"
   - URL: http://127.0.0.1:5000/posts/1
