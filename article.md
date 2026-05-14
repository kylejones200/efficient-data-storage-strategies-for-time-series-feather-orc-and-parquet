# Efficient Data Storage Strategies for Time Series: Feather, ORC, and Parquet Everyone defaults to CSV when they start with data science. But it is
far from the most efficient data storage format.

### Efficient Data Storage Strategies for Time Series: Feather, ORC, and Parquet
Everyone defaults to CSV when they start with data science. But it is far from the most efficient data storage format.


<figcaption>Photo by <a class="markup--anchor markup--figure-anchor" rel="photo-creator noopener" target="_blank">Mika Baumeister</a> on <a class="markup--anchor markup--figure-anchor"


As you advance in your data science journey, you should check out alternative file storage options. CSV or Excel struggle with large datasets due to slow read/write speeds and lack of optimized compression --- which is a problem since time series data often consists of lots of rows (Millions-billions of rows is common for things like IoT and finance), frequent reads/writes, and bloat (raw time series data is often needlessly large).

### Feather: High-Speed Storage for Python and R
Feather is a lightweight, high-speed file format designed for interoperability between pandas (Python) and R. It is based on Apache Arrow, an in-memory columnar format optimized for fast data interchange.

Feather is fast and well-suited for in-memory analytics (like python). It isn't designed for "big data" projects that use spark or hadoop.

### ORC (Optimized Row Columnar): Designed for Big Data
Apache ORC (Optimized Row Columnar) was developed for Hadoop and big data environments, primarily used in systems like Apache Hive, Presto, and AWS Athena.

The columnar format reduces storage space and works well for indexing (provided you know the query patterns that will be used with the data).

> *Note:* *ORC support in pandas is relatively new, and you may need
> to install additional dependencies
> (`pip install pyarrow`).*

### Parquet: The Best of Both Worlds for Analytics?
Apache Parquet is a widely used columnar format designed for high-performance analytics, making it the go-to choice for cloud and big data systems. It is natively supported in pandas, Spark, and AWS Athena.

Parquet stores data in a compressed columnar format and has native support for python and big data tools (Spark, Dask, Hive).

It has clearly won the "battle of the data formats" and is the baseline for cloud workloads like AWS S3, Google BigQuery, and Snowflake.\ \ It is designed for scale, but it can add bloat/overhead for simple cases.

### Performance Comparison: CSV vs. Feather vs. ORC vs. Parquet
Let's compare the performance of these formats in terms of read/write speed and storage size.

We are using the IMDb dataset as an example.



Each format is about 2x faster than CSV.


### Choosing the Right Format


### Conclusion
The choice of storage format matters for the performance, scalability, and efficiency of time series analysis. Feather is best for in-memory workflows, ORC excels in big data environments, and Parquet offers the best balance of efficiency and interoperability.
