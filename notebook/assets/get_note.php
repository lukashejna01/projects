<?php

/**
 * 
 * Získá jednu poznámku z databáze
 * 
 * @param object $connection - napojení na databázi
 * @param integer $id - id jedné poznámky
 * 
 * @return mixed asociativní pole obsahující název a obsah poznámky
 * 
 */

function getNote($connection, $id) {
    $sql = "SELECT *
            FROM note
            WHERE id = ?";
    
    $stmt = mysqli_prepare($connection, $sql);

    if (!$stmt) {
        echo mysqli_error($connection);
    } else {
        mysqli_stmt_bind_param($stmt, "i", $id);

        if (mysqli_execute($stmt)) {
            $result = mysqli_stmt_get_result($stmt);
            return mysqli_fetch_assoc($result);
        }
    }
}