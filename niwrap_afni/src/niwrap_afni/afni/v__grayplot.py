# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__GRAYPLOT_METADATA = Metadata(
    id="958c86831f7afb5a52d51364d6b986bef43d3733.boutiques",
    name="@grayplot",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


VGrayplotParameters = typing.TypedDict('VGrayplotParameters', {
    "__STYX_TYPE__": typing.Literal["@grayplot"],
    "dirname": str,
    "pvorder": bool,
    "peelorder": bool,
    "ijkorder": bool,
    "allorder": bool,
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "@grayplot": v__grayplot_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "@grayplot": v__grayplot_outputs,
    }.get(t)


class VGrayplotOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__grayplot(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    grayplot_img: OutputPathType
    """Output grayplot image"""


def v__grayplot_params(
    dirname: str,
    pvorder: bool = False,
    peelorder: bool = False,
    ijkorder: bool = False,
    allorder: bool = False,
) -> VGrayplotParameters:
    """
    Build parameters.
    
    Args:
        dirname: Directory containing afni_proc.py results.
        pvorder: Within each partition, voxels are ordered by a simple\
            similarity measure.
        peelorder: Within each partition, voxels are ordered by how many 'peel'\
            operations are needed to reach a given voxel.
        ijkorder: Within each partition, voxels are ordered by the 3D index in\
            which they appear in the dataset.
        allorder: Create grayplots for all ordering methods.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@grayplot",
        "dirname": dirname,
        "pvorder": pvorder,
        "peelorder": peelorder,
        "ijkorder": ijkorder,
        "allorder": allorder,
    }
    return params


def v__grayplot_cargs(
    params: VGrayplotParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("@grayplot")
    cargs.append(params.get("dirname"))
    if params.get("pvorder"):
        cargs.append("-pvorder")
    if params.get("peelorder"):
        cargs.append("-peelorder")
    if params.get("ijkorder"):
        cargs.append("-ijkorder")
    if params.get("allorder"):
        cargs.append("-ALLorder")
    return cargs


def v__grayplot_outputs(
    params: VGrayplotParameters,
    execution: Execution,
) -> VGrayplotOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VGrayplotOutputs(
        root=execution.output_file("."),
        grayplot_img=execution.output_file("Grayplot.errts.*.png"),
    )
    return ret


def v__grayplot_execute(
    params: VGrayplotParameters,
    execution: Execution,
) -> VGrayplotOutputs:
    """
    Script to read files from an afni_proc.py results directory and produce a
    grayplot from the errts dataset(s), combined with a motion magnitude indicator
    graph.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VGrayplotOutputs`).
    """
    params = execution.params(params)
    cargs = v__grayplot_cargs(params, execution)
    ret = v__grayplot_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__grayplot(
    dirname: str,
    pvorder: bool = False,
    peelorder: bool = False,
    ijkorder: bool = False,
    allorder: bool = False,
    runner: Runner | None = None,
) -> VGrayplotOutputs:
    """
    Script to read files from an afni_proc.py results directory and produce a
    grayplot from the errts dataset(s), combined with a motion magnitude indicator
    graph.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        dirname: Directory containing afni_proc.py results.
        pvorder: Within each partition, voxels are ordered by a simple\
            similarity measure.
        peelorder: Within each partition, voxels are ordered by how many 'peel'\
            operations are needed to reach a given voxel.
        ijkorder: Within each partition, voxels are ordered by the 3D index in\
            which they appear in the dataset.
        allorder: Create grayplots for all ordering methods.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VGrayplotOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__GRAYPLOT_METADATA)
    params = v__grayplot_params(
        dirname=dirname,
        pvorder=pvorder,
        peelorder=peelorder,
        ijkorder=ijkorder,
        allorder=allorder,
    )
    return v__grayplot_execute(params, execution)


__all__ = [
    "VGrayplotOutputs",
    "VGrayplotParameters",
    "V__GRAYPLOT_METADATA",
    "v__grayplot",
    "v__grayplot_params",
]
