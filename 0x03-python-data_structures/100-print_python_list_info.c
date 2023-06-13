#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (i = 0; i <= size; i++)
	{
		printf("Element %i: %s\n", i, obj->ob_item[i]->ob_type->tp_name)
	}
}
