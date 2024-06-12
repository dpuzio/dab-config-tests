from pyspark.sql import SparkSession


def get_count(table_identifier: str, spark_session: SparkSession):
  return spark_session.read.table(table_identifier).count()


def main():
  print("Hello!")

if __name__ == "__main__":
  main()
