<?php
$py = 'python3 avito.py';

$score = floatval($_POST['score']);
$category_id = intval($_POST['category_id']);
$has_diff_location = isset($_POST['has_diff_location']) ? 1 : 0;
$uncounted = intval($_POST['uncounted']);
$count_procent = floatval($_POST['count_procent'] / 100);
$bad_item = isset($_POST['bad_item']) ? 1 : 0;
$model = $_POST['model'];

$params = array(
    'score' => array($score),
    'category_id' => array($category_id),
    'has_diff_location' => array($has_diff_location),
    'uncounted' => array($uncounted),
    'count_procent' => array($count_procent),
    'bad_item' => array($bad_item),
    'model' => array($model)
);

$paramsJson = json_encode($params);

$command = $py . ' ' . escapeshellarg($paramsJson);

$result = exec($command, $output, $returnCode);

echo json_encode($result);