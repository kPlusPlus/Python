require 'vendor/autoload.php';

use Aws\Sns\SnsClient; 
use Aws\Exception\AwsException;

/**

docs.aws.amazon.com/code-library/latest/ug/sns_example_sns_ConfirmSubscription_section.html

 * Verifies an endpoint owner's intent to receive messages by validating the token sent to the endpoint by an earlier Subscribe action.
 *
 * This code expects that you have AWS credentials set up per:
 * https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/guide_credentials.html
 */
 
$SnSclient = new SnsClient([
    'profile' => 'default',
    'region' => 'eu-central-1',
    'version' => '2010-03-31'
]);

$subscription_token = 'arn:aws:sns:eu-central-1:266061335929:development-topic:f2fd8355-be1a-4f82-b88e-7571b54109cd';
$topic = 'arn:aws:sns:eu-central-1:266061335929:development-topic';

try {
    $result = $SnSclient->confirmSubscription([
        'Token' => $subscription_token,
        'TopicArn' => $topic,
    ]);
    var_dump($result);
} catch (AwsException $e) {
    // output error message if fails
    error_log($e->getMessage());
} 

