# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_AA_SHRINKWRAP_METADATA = Metadata(
    id="f1b620c2d26413faf9fc31bd238562722d3919d1.boutiques",
    name="mris_AA_shrinkwrap",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MrisAaShrinkwrapParameters = typing.TypedDict('MrisAaShrinkwrapParameters', {
    "__STYX_TYPE__": typing.Literal["mris_AA_shrinkwrap"],
    "t1_vol": InputPathType,
    "pd_vol": InputPathType,
    "output_dir": str,
    "omit_self_intersection": bool,
    "create_curvature_area": bool,
    "average_curvature": typing.NotRequired[float | None],
    "white_only": bool,
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
        "mris_AA_shrinkwrap": mris_aa_shrinkwrap_cargs,
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
    }.get(t)


class MrisAaShrinkwrapOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_aa_shrinkwrap(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mris_aa_shrinkwrap_params(
    t1_vol: InputPathType,
    pd_vol: InputPathType,
    output_dir: str,
    omit_self_intersection: bool = False,
    create_curvature_area: bool = False,
    average_curvature: float | None = 10,
    white_only: bool = False,
) -> MrisAaShrinkwrapParameters:
    """
    Build parameters.
    
    Args:
        t1_vol: T1 volume file.
        pd_vol: PD volume file.
        output_dir: Output directory.
        omit_self_intersection: Omit self-intersection and only generate\
            gray/white surface.
        create_curvature_area: Create curvature and area files from white\
            matter surface.
        average_curvature: Average curvature values a specified number of times\
            (default=10).
        white_only: Only generate white matter surface.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_AA_shrinkwrap",
        "t1_vol": t1_vol,
        "pd_vol": pd_vol,
        "output_dir": output_dir,
        "omit_self_intersection": omit_self_intersection,
        "create_curvature_area": create_curvature_area,
        "white_only": white_only,
    }
    if average_curvature is not None:
        params["average_curvature"] = average_curvature
    return params


def mris_aa_shrinkwrap_cargs(
    params: MrisAaShrinkwrapParameters,
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
    cargs.append("mris_AA_shrinkwrap")
    cargs.append(execution.input_file(params.get("t1_vol")))
    cargs.append(execution.input_file(params.get("pd_vol")))
    cargs.append(params.get("output_dir"))
    if params.get("omit_self_intersection"):
        cargs.append("-q")
    if params.get("create_curvature_area"):
        cargs.append("-c")
    if params.get("average_curvature") is not None:
        cargs.extend([
            "-a",
            str(params.get("average_curvature"))
        ])
    if params.get("white_only"):
        cargs.append("-whiteonly")
    return cargs


def mris_aa_shrinkwrap_outputs(
    params: MrisAaShrinkwrapParameters,
    execution: Execution,
) -> MrisAaShrinkwrapOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisAaShrinkwrapOutputs(
        root=execution.output_file("."),
    )
    return ret


def mris_aa_shrinkwrap_execute(
    params: MrisAaShrinkwrapParameters,
    execution: Execution,
) -> MrisAaShrinkwrapOutputs:
    """
    This program positions the tessellation of the cortical surface at the white
    matter surface, then the gray matter surface and generates surface files for
    these surfaces as well as a 'curvature' file for the cortical thickness, and a
    surface file which approximates layer IV of the cortical sheet.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisAaShrinkwrapOutputs`).
    """
    params = execution.params(params)
    cargs = mris_aa_shrinkwrap_cargs(params, execution)
    ret = mris_aa_shrinkwrap_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_aa_shrinkwrap(
    t1_vol: InputPathType,
    pd_vol: InputPathType,
    output_dir: str,
    omit_self_intersection: bool = False,
    create_curvature_area: bool = False,
    average_curvature: float | None = 10,
    white_only: bool = False,
    runner: Runner | None = None,
) -> MrisAaShrinkwrapOutputs:
    """
    This program positions the tessellation of the cortical surface at the white
    matter surface, then the gray matter surface and generates surface files for
    these surfaces as well as a 'curvature' file for the cortical thickness, and a
    surface file which approximates layer IV of the cortical sheet.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        t1_vol: T1 volume file.
        pd_vol: PD volume file.
        output_dir: Output directory.
        omit_self_intersection: Omit self-intersection and only generate\
            gray/white surface.
        create_curvature_area: Create curvature and area files from white\
            matter surface.
        average_curvature: Average curvature values a specified number of times\
            (default=10).
        white_only: Only generate white matter surface.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisAaShrinkwrapOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_AA_SHRINKWRAP_METADATA)
    params = mris_aa_shrinkwrap_params(
        t1_vol=t1_vol,
        pd_vol=pd_vol,
        output_dir=output_dir,
        omit_self_intersection=omit_self_intersection,
        create_curvature_area=create_curvature_area,
        average_curvature=average_curvature,
        white_only=white_only,
    )
    return mris_aa_shrinkwrap_execute(params, execution)


__all__ = [
    "MRIS_AA_SHRINKWRAP_METADATA",
    "MrisAaShrinkwrapOutputs",
    "MrisAaShrinkwrapParameters",
    "mris_aa_shrinkwrap",
    "mris_aa_shrinkwrap_params",
]
