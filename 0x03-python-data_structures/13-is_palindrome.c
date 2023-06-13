#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: a pointer to the singly linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int length, i, x, y;
	listint_t *start;
	listint_t *end;

	start = *head;
	length = 0;
	while (start != NULL)
	{
		start = start->next;
		length++;
	}
	if(length == 0)
		return (1);
	for (i = 0; i < length / 2; i++)
	{
		start = *head;
		end = *head;
		for (x = 0; x < i; x++)
			start = start->next;
		for (y = 0; y < length - 1 - i; y++)
			end = end->next;
		if (start->n != end->n)
			return (0);
	}
	return (1);
}
