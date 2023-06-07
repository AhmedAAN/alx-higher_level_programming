#include "lists.h"

/**
 * insert_node - a function that inserts a number into a sorted singly linked list
 * @head: a pointer to the haed of the list
 * @number: the value of the added node
 *
 * Return: the address to the new node, or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *previous, current, new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	previous = NULL;
	current = *head;
	while (current != NULL && current->n < number)
	{
		previous = current;
		current = current->next;
	}
	if (previous == NULL)
	{
		new->next = current;
		*head = new;
		return (new);
	}
	previous->next = new;
	new->next = current;
	return (new);
}
