SELECT
    [io_stall_read_ms] =
        CASE WHEN [num_of_reads] = 0
            THEN 0 ELSE [io_stall_read_ms] END,
    [num_of_reads] =
        CASE WHEN [num_of_reads] = 0
            THEN 0 ELSE [num_of_reads] END,
    [io_stall_write_ms] =
        CASE WHEN [num_of_reads] = 0
            THEN 0 ELSE [io_stall_write_ms] END,
    [num_of_writes] =
        CASE WHEN [num_of_reads] = 0
            THEN 0 ELSE [num_of_writes] END,
    [io_stall] =
        CASE WHEN [num_of_reads] = 0
            THEN 0 ELSE [io_stall] END,

    LEFT ([mf].[physical_name], 2) AS [Drive],
    DB_NAME ([vfs].[database_id]) AS [DB],
    [mf].[physical_name]
FROM
    sys.dm_io_virtual_file_stats (NULL,NULL) AS [vfs]
JOIN sys.master_files AS [mf]
    ON [vfs].[database_id] = [mf].[database_id]
    AND [vfs].[file_id] = [mf].[file_id]
    WHERE [vfs].[file_id] = 1 -- log files
-- ORDER BY [Latency] DESC
-- ORDER BY [ReadLatency] DESC
ORDER BY [io_stall_read_ms] DESC;
GO