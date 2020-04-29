#include "lists.h"
#include <stdio.h>

int check_cycle(listint_t *list)
{
listint_t *s = list, *f = list;

while (s && f && f->next)
{
s = s->next->next;
f = f->next;
if (s == f->next)
{
return (1);
}
}
return (0);
}
/*
    while (slow_p && fast_p && fast_p->next) { 
        slow_p = slow_p->next; 
        fast_p = fast_p->next->next; 
        if (slow_p == fast_p) { 

            return 1; 
        } 
    } 
    return 0; 
} 
*/