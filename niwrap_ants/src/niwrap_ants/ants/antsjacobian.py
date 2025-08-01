# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

ANTSJACOBIAN_METADATA = Metadata(
    id="4c1495ce17166625b172b3fbe727bd30b17f079f.boutiques",
    name="ANTSJacobian",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)


AntsjacobianParameters = typing.TypedDict('AntsjacobianParameters', {
    "__STYXTYPE__": typing.Literal["ANTSJacobian"],
    "imagedim": int,
    "gwarp": InputPathType,
    "outfile": str,
    "uselog": int,
    "maskfn": InputPathType,
    "normbytotalbool": int,
    "projectionvector": typing.NotRequired[str | None],
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
        "ANTSJacobian": antsjacobian_cargs,
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
        "ANTSJacobian": antsjacobian_outputs,
    }.get(t)


class AntsjacobianOutputs(typing.NamedTuple):
    """
    Output object returned when calling `antsjacobian(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    jacobian_output: OutputPathType
    """Output file containing the Jacobian determinant information."""


def antsjacobian_params(
    imagedim: int,
    gwarp: InputPathType,
    outfile: str,
    uselog: int,
    maskfn: InputPathType,
    normbytotalbool: int,
    projectionvector: str | None = None,
) -> AntsjacobianParameters:
    """
    Build parameters.
    
    Args:
        imagedim: The dimensionality of the input image.
        gwarp: The input warp image.
        outfile: The prefix for the output files.
        uselog: Whether to use logarithm in computation.
        maskfn: Mask file used in the computation.
        normbytotalbool: Normalize the Jacobian by the total in the mask. Use\
            this to adjust for head size.
        projectionvector: Projects the warp along the specified direction. Do\
            not add this option if no projection is desired.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "ANTSJacobian",
        "imagedim": imagedim,
        "gwarp": gwarp,
        "outfile": outfile,
        "uselog": uselog,
        "maskfn": maskfn,
        "normbytotalbool": normbytotalbool,
    }
    if projectionvector is not None:
        params["projectionvector"] = projectionvector
    return params


def antsjacobian_cargs(
    params: AntsjacobianParameters,
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
    cargs.append("ANTSJacobian")
    cargs.append(str(params.get("imagedim")))
    cargs.append(execution.input_file(params.get("gwarp")))
    cargs.append(params.get("outfile"))
    cargs.append(str(params.get("uselog")))
    cargs.append(execution.input_file(params.get("maskfn")))
    cargs.append(str(params.get("normbytotalbool")))
    if params.get("projectionvector") is not None:
        cargs.append(params.get("projectionvector"))
    return cargs


def antsjacobian_outputs(
    params: AntsjacobianParameters,
    execution: Execution,
) -> AntsjacobianOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = AntsjacobianOutputs(
        root=execution.output_file("."),
        jacobian_output=execution.output_file(params.get("outfile") + "Jacobian.nii.gz"),
    )
    return ret


def antsjacobian_execute(
    params: AntsjacobianParameters,
    execution: Execution,
) -> AntsjacobianOutputs:
    """
    Calculate the Jacobian determinant of a transformation using ANTs. WARNING:
    ANTSJacobian may not be working correctly; see CreateJacobianDeterminantImage
    for an alternative method.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `AntsjacobianOutputs`).
    """
    params = execution.params(params)
    cargs = antsjacobian_cargs(params, execution)
    ret = antsjacobian_outputs(params, execution)
    execution.run(cargs)
    return ret


def antsjacobian(
    imagedim: int,
    gwarp: InputPathType,
    outfile: str,
    uselog: int,
    maskfn: InputPathType,
    normbytotalbool: int,
    projectionvector: str | None = None,
    runner: Runner | None = None,
) -> AntsjacobianOutputs:
    """
    Calculate the Jacobian determinant of a transformation using ANTs. WARNING:
    ANTSJacobian may not be working correctly; see CreateJacobianDeterminantImage
    for an alternative method.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        imagedim: The dimensionality of the input image.
        gwarp: The input warp image.
        outfile: The prefix for the output files.
        uselog: Whether to use logarithm in computation.
        maskfn: Mask file used in the computation.
        normbytotalbool: Normalize the Jacobian by the total in the mask. Use\
            this to adjust for head size.
        projectionvector: Projects the warp along the specified direction. Do\
            not add this option if no projection is desired.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AntsjacobianOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ANTSJACOBIAN_METADATA)
    params = antsjacobian_params(
        imagedim=imagedim,
        gwarp=gwarp,
        outfile=outfile,
        uselog=uselog,
        maskfn=maskfn,
        normbytotalbool=normbytotalbool,
        projectionvector=projectionvector,
    )
    return antsjacobian_execute(params, execution)


__all__ = [
    "ANTSJACOBIAN_METADATA",
    "AntsjacobianOutputs",
    "AntsjacobianParameters",
    "antsjacobian",
    "antsjacobian_params",
]
