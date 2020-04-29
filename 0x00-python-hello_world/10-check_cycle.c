#include "lists.h"
#include <stdio.h>

int check_cycle(listint_t *list)
{
listint_t *s = list, *f = list;

if (!list)
return (0);
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
