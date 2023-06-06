#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: a pointer to the begining of the list
 * Return: 0 if there is no loop or 1 if there is loop
 *
 */
int check_cycle(listint_t *list)
{
	listint_t *current;
	int check;

	if (!list)
		return (0);
	current = list;
	check = current->n;

	current = current->next;
	while (current != NULL)
	{
		if (current->n == check)
			return (1);
		current = current->next;
	}

	return (0);
}
