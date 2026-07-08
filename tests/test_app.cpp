#include "app.hpp"

int main()
{
    if (add(2, 3) != 5)
    {
        return 1;
    }

    if (add(-1, 1) != 0)
    {
        return 1;
    }

    return 0;
}
