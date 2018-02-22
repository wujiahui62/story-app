<head><title>Story List</title></head>
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<body>
<div class="w3-margin">
  <table>
    <tr>
      <form action="/edit-story/{{story['_id']}}" method="post">
      <td>
        <div class="w3-card-4 w3-padding">
          <input autofocus type="text" name="new_book" placeholder="{{story['book']}}" style="min-width: 400px">
        </div>
      </td>
       <td>
        <div class="w3-card-4 w3-padding">
          <input autofocus type="text" name="new_theme" placeholder="{{story['theme']}}" style="min-width: 400px">
        </div>
      </td>
      <td>
        <div class="w3-padding w3-center">
          <input type="image" src="/static/save-task.png"/>
        </div>
      </td>
        </form>
    </tr>
  </table>
</body>