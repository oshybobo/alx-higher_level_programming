#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - confirms the cyclic nature of the singly linked list
 * Return: 0 - no cycle, 1 if cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	if(!list)
	{
		return (0);
	}

	while
	{
		if (fast->next != NULL && fast->next->next != NULL)
		{

			fast = fast->next->next;
			slow = slow->next;

			if (fast == slow) 
			{
				return (1);
			}
	
		}

		else
		{
			return (0);
		}

	}

