using namespace std;

int bin_search(int a[], int el, int index, int n)
{
    int low = index;
    int high = n - 1;
    int mid = (high + low) / 2;
    while ((low < high) and (a[mid] != el))
    {
        if (el > a[mid])
        {
            low = mid + 1;
        }

        else
        {
            high = mid - 1;
        }
        mid = (low + high) / 2;
    }
    return mid;
}

int* prefix_sum(char element, string s, int n)
{
    int* array = new int[n];


    int last = 0;

    for (int i = 0; i < n; i++) {
        if (s[i] != element) { last += 1; }
        array[i] = last;
    }
    return array;

}
int main()
{
    int k;
    cin >> k;
    string s;
    cin >> s;
    int n = s.size();
    int max_ = 0;

    char lang[26] = { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' };

    for (int i = 0; i < 26; i++)
    {
        int* array;
        array = prefix_sum(lang[i], s, n);
        for (int j = 0; j < n; j++)
        {
                int last_ = 0;
                if ( s[j] == lang[i] ) 
                {
                last_ = bin_search(array, (array[j] + k), j, n);
                }
                else
                { last_ = bin_search(array, array[j] + k -1, j, n);}
                while (last_ < n - 1 and array[last_ + 1] == array[last_])
                {
                    last_ += 1;
                }

            


                if (last_ - j  + 1 > max_)
                {
                    max_ = last_ - j + 1;
                }

            

        }
    }
    cout << max_;
}