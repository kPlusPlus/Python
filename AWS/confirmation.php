<?php
// Handle the subscription confirmation request
$confirmationToken = $_POST['Token']; // Assuming AWS sends the confirmation token in the POST request

if ($confirmationToken) {
    // Confirm the subscription by echoing the token
    echo "SubscriptionConfirmation";
    echo "Token: $confirmationToken";
} else {
    // Handle other SNS messages (e.g., notifications)
    // Your code to process SNS messages here

	echo "Notification work";
}

