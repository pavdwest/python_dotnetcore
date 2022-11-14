DateTime t0 = DateTime.Now;
int maxNumber = 20;
bool found = false;
long start = maxNumber;

while (!found)
{
    found = true;
    int i = 2;
    while ((i < maxNumber + 1) && found)
    {
        if (start % i != 0)
        {
            found = false;
        }
        i++;
    }
    start++;
}

Console.WriteLine("Answer: {0}", start - 1);
Console.WriteLine("Time taken: {0:N5}", (DateTime.Now - t0).TotalSeconds);
