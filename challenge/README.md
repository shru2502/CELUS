# Cake Logbook

At CELUS we are very much into cakes, and usually, there is not a week that goes by without someone bringing a cake,
with some days sporting multiple baked goods on display. That is a serious matter to us. It goes so far that we have
developed internal software to track cake donations (that part is actually true, by the way!).

But not all is powdered sugar and happiness... See, the problem is, people are usually way more preoccupied with baking
and consumption than they are with data entry, which leads to many data inconsistencies and poor data quality on our old
cake logbook, which was maintained as an excel sheet before our cake software was developed. Adding the fact that our
team is very international, and therefore uses different units, this leads to an even more problematic situation (I
know, a cookie mistake, right?)

That is where you come in, you are tasked with loading this old data, exported as a CSV file named `cake_data.csv`, into
the current's system SQL database, so we don't lose any historical data.

---------------------

For this challenge you will need to connect to a postgresql DB (`'postgresql://postgres:postgres@localhost'`). 
Where you should store the cakes' data. The simplest way to achieve that is to
install docker engine on your machine (available for pretty much any OS and distribution) and run the postgres container
like this:

```shell
docker run -ti --network=host --name local-postgres -e POSTGRES_PASSWORD=postgres -d postgres
```

Important Notes: 
* Please, do not change the default url to connect to the DB.
* The provided file is a sample, and the actual database will have millions of records.

While doing this challenge, please:

- Do it yourself, without help from others and without copying solutions from elsewhere
- Make sure that it runs and do not rename or move the `main.py` file or the `etl` package. Challenges that do not run
  will not be reviewed
- If you add any dependencies, remember to include them on the `requirements.txt` file
- Please do not publicly disclose this challenge or your solution to it :)

## 1. Extract, transform and load the data into our database

The main structure of the code is there, and you are asked to complete the extractor, transformer and loader modules so
we can migrate the whole legacy cake data into the new system.

There are a few points to be observed:

1. If no units are mentioned on a cake, you can assume millimeters, as that is the standard.
2. Regardless of the original data's unit, store the cake size converted to millimeters on the database.
3. Try to parse as much of the data as possible, but:
    - Do not add items that you cannot be certain about the cake size. For example, if a cake has the value '20mm', but
      the unit field is 'inches', it is not possible to be certain which unit the cake really has, so you should skip
      this entry. Same thing for any other type of irrecoverable data quality issues, such as the value being reported
      as 'big', or unit being reported as "Jonas' clenched fist".
    - You should still include cakes even if you cannot be sure about the flavour or the vegan status. Store those
      fields as null on those cases.
    - Use your common sense. Be as flexible as possible, if things could be safely assumed, but do not assume or make-up
      values that you cannot be sure about.
    - The name field should receive only valid flavours (`VALID_CAKE_FLAVORS`)

## 2. Store the original unit

Many users requested to be able to see the cake information on the software in the original unit that it was entered on,
and for that, you are asked to:

1. add a new field to the database document (and accompanying ORM model) called `original_unit`, of string type that
   could receive the values `mm`, `in` and `m` only.
2. populate the new field with the data from the file

## 3. Test case

To ensure long-tem maintainability of your ETL code, and to double-check that it works as it should, you are asked to
write a few unit test cases. Please include instructions on how to run them.

## 4. Use postgresql to build a report

Use postgresql to build a report about the imported data so users can be made aware of general cake information. Use your
best judgment on what would be the best data to display and how to display it, but you are asked to at the very least
show a list of possible cakes filled in error, whose data might not make sense, so people can double-check them manually
on the company photos to see if there is any mismatch.

Furthermore, please handle the following specific SQL queries. Write your queries in the `queries.sql` file, ensuring each query is placed under its corresponding comment. Please retain the comments for each query.
1. Find the largest cake for the top 5 flavors.
2. Determine which flavors have the highest number of vegan cakes.
3. Identify the cake flavor of the first and last entries for each month.
4. Determine the month with the highest number of cakes and the one with the least.

Please note that the queries should be optimized, as they will be run on a database consisting of millions of cakes' data, not just the ones presented in the CSV file. Additionally, feel free to append the required indexes either at the end of `queries.sql` or in a separate file.
## 5. Question

Briefly answer: How could this ETL setup be improved? Are there any tools or frameworks that could be added?
