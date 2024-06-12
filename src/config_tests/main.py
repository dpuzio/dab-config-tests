from pyspark.sql import SparkSession
import argparse
from pyhocon import ConfigFactory

# def get_count(table_identifier: str, spark_session: SparkSession):
#     return spark_session.read.table(table_identifier).count()


def main():
    # TODO:
    # 2. use hocon to read conf files
    # 3. test it we can get parameters in the spark job
    # 4. showcase how to parametrize SQL statement
    # 5. suggest a better hocon files organization (e.g. with nested structures)
    # 6. showcase local unit testing

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--config_file_path", type=str, required=True)

    args = parser.parse_args()
    config_file_path = args.config_file_path
    print(f'Reading configuration from {config_file_path}')

    config = ConfigFactory.parse_file(f'/Workspace/{config_file_path}')
    schema_name = config.get('schema_name')
    print(f'Parsed out schema name: {schema_name}')

    spark_session = SparkSession.builder.getOrCreate()



if __name__ == "__main__":
    main()
