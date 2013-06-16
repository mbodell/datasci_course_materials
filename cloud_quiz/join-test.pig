register s3n://uw-cse-344-oregon.aws.amazon.com/myudfs.jar

-- load the test file into Pig
raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/cse344-test-file' USING TextLoader as (line:chararray);
-- later you will load to other files, example:
--raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/btc-2010-chunk-000' USING TextLoader as (line:chararray); 

-- parse each line into ntriples
ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);

--filter the information
filt_trip = filter ntriples by subject matches '.*business.*';

--make the 2nd copy
filt_trip2 = foreach filt_trip generate subject as subject2, predicate as predicate2, object as object2;

--calculate the join result
join_result = join filt_trip BY subject, filt_trip2 BY subject2 PARALLEL 50;

-- store the results in the folder /user/hadoop/example-results
store join_result into '/user/hadoop/example-results' using PigStorage();
-- Alternatively, you can store the results in S3, see instructions:
-- store count_by_object_ordered into 's3n://superman/example-results';
