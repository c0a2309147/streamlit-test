#include </usr/include/python3.10/Python.h>

//メインの処理
int cal(int a, int b, int c, int d)
{
	int kekka;
	kekka = (a + b + c + d) / 4;
	return kekka;
}
//変換
static PyObject* pyadd(PyObject* self, PyObject* args)
{
	
	int a, b, c, d, kekka;
	if (!PyArg_ParseTuple(args, "iiii", &a, &b, &c, &d))
	{
		return NULL;	
	}
	
	kekka = cal(a, b, c, d);
	
	
	//メインの処理からreturnしたい値
	return Py_BuildValue("i", kekka);
}

//関数の設定
static PyMethodDef calMethod[] = {
    { "cal", pyadd, METH_VARARGS},
    { NULL }
};


//モジュールの定義
static struct PyModuleDef calModule = {
    PyModuleDef_HEAD_INIT,
    "calModule",
    "Python3 C API Module(Sample 2)",
    -1,
    calMethod
};

PyMODINIT_FUNC PyInit_calModule(void)
{
    return PyModule_Create(&calModule);
}