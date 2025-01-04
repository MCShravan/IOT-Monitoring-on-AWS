import boto3
import random
import time
import json

def generate_data():
    kinesis_client = boto3.client('kinesis', region_name='us-east-1') 
    stream_name = 'IoTStream' 

    end_time = time.time() + 60  # Run for 60 seconds
    while time.time() < end_time:
        data = {
            'device_id': random.randint(1, 100),
            'temperature': round(random.uniform(20.0, 30.0), 2),
            'humidity': round(random.uniform(30.0, 50.0), 2),
            'timestamp': time.time()
        }
        print(f"Sending data: {data}")
        kinesis_client.put_record(
            StreamName=stream_name,
            Data=json.dumps(data),
            PartitionKey='partitionKey'
        )
        time.sleep(1)  # Wait for 1 second between records

generate_data()
