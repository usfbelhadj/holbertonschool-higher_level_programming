#include "lists.h"
#include <stdio.h>

int check_cycle(listint_t *list)
{
listint_t *s = list, *f = list;

while (s && f->next)
{
s = s->next->next;
if (s == f->next)
{
return (1);
}
}
return (0);
}
