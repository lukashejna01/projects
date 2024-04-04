<?php

require "assets/database.php";

$sql = "SELECT * 
        FROM note
        ORDER BY note_date DESC";

$result = mysqli_query($connection, $sql);

$task = mysqli_fetch_all($result, MYSQLI_ASSOC);

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $sql = "INSERT INTO note (note_name, note_content, note_date)
            VALUES  (?, ?, ?)";

    $statement = mysqli_prepare($connection, $sql);

    mysqli_stmt_bind_param($statement, "sss", $_POST["note_name"], $_POST["note_content"], date("Y-m-d H:i:s"));

    mysqli_execute($statement);
    $id = mysqli_insert_id($connection);
    header("location: index.php");
}

?>


<!DOCTYPE html>
<html lang="cs-cz">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles-main.css?v=<?= filemtime('styles-main.css'); ?>">
    <title>Poznámkový blok</title>
</head>
<body>
    <header>
        <h1>Poznámkový blok</h1>
    </header>
    <main>
        <section class="add-note">
            <h2>Přidat novou poznámku</h2>
            <form action="" method="POST">
                <input type="text" name="note_name" class="note-input" placeholder="Název poznámky" autocomplete="off" required><br>
                <textarea name="note_content" class="note-textarea" placeholder="Obsah poznámky"></textarea><br>
                <input type="submit" value="Přidat" class="btn-submit">
            </form>
        </section>
        <section class="note-list">
            <h2>Poznámky</h2>
            <ul class="note-ul">
                <?php foreach ($task as $one_task): ?>
                    <li class="note-item">
                        <div class="one_task">
                            <h2 class="note-name"><?= $one_task["note_name"]; ?></h2>
                            <p class="note-date"><?= date("d.m.Y H:i:s", strtotime($one_task["note_date"])); ?></p>
                            <p class="note-content"><?= $one_task["note_content"]; ?></p>
                        </div>
                        <a href="one_note.php?id=<?= $one_task["id"]; ?>" class="btn-edit">Upravit</a>
                    </li>
                <?php endforeach; ?>
            </ul>
        </section>
    </main>
</body>
</html>
