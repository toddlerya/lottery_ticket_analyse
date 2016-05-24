#!/usr/bin/php

<?php 
/**
 * [$data 生成格式json]
 * @var array
 */
$data = [];
$logs = explode(PHP_EOL, file_get_contents('../../history_ticket.log') );
foreach ($logs as $key => $value) {
	if(($value = trim($value))){
		preg_match('/^(.{10})\((\d{5,8})\)\sblue\:(\d{1,2})\s-\sred\:(.+)$/', $value , $result);
		$data[] = ['date' => $result[1],'cycle' => $result[2],'blue' => $result[3],'red' => explode(',', $result[4])];
	}
	
}
file_put_contents('../data.json',json_encode($data));