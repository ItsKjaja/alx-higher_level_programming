#include "lists.h"


/**
 * check_cycle - checking if a linked list contains a cycle
 * @list: linked list to be checked
 *
 * Return: 1 if the list has a cycle, 0 if not
 */



int check_cycle(listint_t *list)
{
	listint_t *cyc;

	if (!list)
		return (0);

	while (list)
	{
		cyc = list;
		list = list->next;
		if (cyc <= list)
			return (1);
	}
	return (0);
}
