<head>
<title>Story List</title>
<meta charset="utf-8"> 
</head>
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<body>
<div class="w3-margin">
  <table>
    <tr>
      <th>
        <a href="/">
        <div width=400 class="w3-card-4 w3-padding" style="min-width: 400px">Story List</div>
        </a>
      </th>
      <form action="/search-results" method="post">
      <th>
        <div class="w3-card-4 w3-padding">
          <input autofocus type="text" name="key" placeholder="Search" style="min-width: 400px">
        </div>
      </th>
      <th>
        <div class="w3-padding w3-center">
          <input type="image" src="/static/save-task.png"/>
        </div>
      </th>

</form>

    </tr>
      <form action="/new-story" method="post">
    <tr>
      <td>
        <div class="w3-card-4 w3-padding">
          <input autofocus type="text" name="book" placeholder="New book..." style="min-width: 400px">
        </div>
      </td>
      <td>
        <div class="w3-card-4 w3-padding">
          <input autofocus type="text" name="theme" placeholder="New theme..." style="min-width: 400px">
        </div>
      </td>
      <td>
        <div class="w3-padding w3-center">
          <input type="image" src="/static/save-task.png"/>
        </div>
      </td>
      </tr>
    %for story in stories:
      <tr>
        <td>
          <div class="w3-card-4 w3-padding">{{story['book']}}</div>
        </td>
        <td>
          <div class="w3-card-4 w3-padding">{{story['theme']}}</div>
        </td>
        <td>
          <div class="w3-padding w3-center">
            <a href="/discard-story/{{story['_id']}}">
              <img src="/static/discard-task.png">
            </a>
          </div>
        </td>
        <td>
          <div class="w3-padding w3-center">
            <a href="/edit-story/{{story['_id']}}">
              <img src="/static/pencil-2x.png"">
            </a>
          </div>
        </td>
      </tr>
    %end
    </form>
  </table>
</body>