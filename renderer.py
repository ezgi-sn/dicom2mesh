import vtk

ColorBackground = [1.0, 1.0, 1.0]

obj_path = "outputs/OBJs/brain_v2.obj"

reader = vtk.vtkOBJReader()

reader.SetFileName(obj_path)

reader.Update()


mapper = vtk.vtkPolyDataMapper()

if vtk.VTK_MAJOR_VERSION <= 5:

     mapper.SetInput(reader.GetOutput())

else:

     mapper.SetInputConnection(reader.GetOutputPort())

actor = vtk.vtkActor()

actor.SetMapper(mapper)

# Create a rendering window and renderer

ren = vtk.vtkRenderer()

ren.SetBackground(ColorBackground)

renWin = vtk.vtkRenderWindow()

renWin.AddRenderer(ren)

# Create a renderwindowinteractor

iren = vtk.vtkRenderWindowInteractor()

iren.SetRenderWindow(renWin)

# Assign actor to the renderer

ren.AddActor(actor)

# Enable user interface interactor

iren.Initialize()

renWin.Render()

iren.Start()