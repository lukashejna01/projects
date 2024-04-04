<?php

require "assets/database.php";
require "assets/get_note.php";

if (mysqli_connect_error()) {
    echo mysqli_connect_error();
    exit();
}

if (isset($_GET["id"]) && is_numeric($_GET["id"])) {
    $note = getNote($connection, $_GET["id"]);

    if ($note) {
        $note_name = $note["note_name"];
        $note_content = $note["note_content"];
        $note_date = $note["note_date"];
        $note_id = $note["id"];
    } else {
        die("Poznámka nenalezena");
    }
} else {
    die("ID nezadáno");
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (isset($_POST["delete"])) {

        $sql_delete = "DELETE FROM note WHERE id = ?";
        $stmt_delete = mysqli_prepare($connection, $sql_delete);
        
        if (!$stmt_delete) {
            echo mysqli_error($connection);
        } else {
            mysqli_stmt_bind_param($stmt_delete, "i", $note_id);

            if (mysqli_stmt_execute($stmt_delete)) {
                header("Location: index.php");
                exit();
            } else {
                echo "Chyba při mazání poznámky: " . mysqli_stmt_error($stmt_delete);
            }
        }
    } else {

        $note_name = $_POST["note_name"];
        $note_content = $_POST["note_content"];

        $sql_update = "UPDATE note
                SET note_name = ?,
                    note_content = ?,
                    note_date = NOW()
                WHERE id = ?";
        
        $stmt_update = mysqli_prepare($connection, $sql_update);
        
        if (!$stmt_update) {
            echo mysqli_error($connection);
        } else {
            mysqli_stmt_bind_param($stmt_update, "ssi", $note_name, $note_content, $note_id);

            if (mysqli_stmt_execute($stmt_update)) {
                $note_check = "Poznámka byla úspěšně aktualizována!";
            } else {
                echo "Chyba při aktualizaci poznámky: " . mysqli_stmt_error($stmt_update);
            }
        }
    }
}

?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles-one-note.css?v=<?= filemtime('styles-one-note.css'); ?>">
    <title>Editace poznámky</title>
</head>
<body>
    <header>
        <h3>Editace poznámky</h3>
    </header>
    <main>
        <section class="note-edit">
            <form method="POST">
                <input type="text" name="note_name" class="note-input" placeholder="Název poznámky" value="<?= htmlspecialchars($note_name); ?>" required><br>
                <input type="text" name="note_content" class="note-input" placeholder="Obsah poznámky" value="<?= htmlspecialchars($note_content); ?>"><br>
                <input type="submit" name="save" value="Uložit" class="btn-save">
                <input type="submit" name="delete" value="Smazat" class="btn-delete">
            </form>
            <a href="index.php" class="btn-back">Zpět</a>
            <?php if($_SERVER["REQUEST_METHOD"] == "POST"): ?>
                <p class="note-check"><?= $note_check ?></p>
            <?php endif; ?>
        </section>
    </main>
</body>
</html>
