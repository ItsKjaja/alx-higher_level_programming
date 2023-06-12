#include <stdlib.h>
#include "lists.h"


/**
 * is_palindrome_rec - check if list is palindrome in recursive way
 * @head: head
 * @last: last ele
 * Return: 0 or 1
 */


int is_palindrome_rec(listint_t **head, listint_t *last)
{
	int is_pali, is_pali1;

	if (last == NULL)
		return (1);
	is_pali = is_palindrome_rec(head, last->next);

	if (is_pali == 0)
		return (0);
	is_pali1 = (*head)->n == last->n;
	*head = (*head)->next;
	return is_pali1;

}


/**
 * is_palindrome - check if linked list palindrome
 * @head: linked list head
 * Retuen: 0 if not palindrome 1 otherwise
 */

int is_palindrome(listint_t **head)
{
	listint_t **el = head;

	return (is_palindrome_rec(el, *head));
}
