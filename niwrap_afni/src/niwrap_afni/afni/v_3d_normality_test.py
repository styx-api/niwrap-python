# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_NORMALITY_TEST_METADATA = Metadata(
    id="25ece735fc7f7a81d4c52176a3e16fdc401aa190.boutiques",
    name="3dNormalityTest",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dNormalityTestParameters = typing.TypedDict('V3dNormalityTestParameters', {
    "__STYX_TYPE__": typing.Literal["3dNormalityTest"],
    "input": InputPathType,
    "prefix": str,
    "noexp": bool,
    "pval": bool,
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
        "3dNormalityTest": v_3d_normality_test_cargs,
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
        "3dNormalityTest": v_3d_normality_test_outputs,
    }.get(t)


class V3dNormalityTestOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_normality_test(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_dataset: OutputPathType
    """Output dataset with results"""


def v_3d_normality_test_params(
    input_: InputPathType,
    prefix: str,
    noexp: bool = False,
    pval: bool = False,
) -> V3dNormalityTestParameters:
    """
    Build parameters.
    
    Args:
        input_: Specifies the input dataset.
        prefix: Specifies the name for the output dataset.
        noexp: Do not convert the A-D statistic to an exponentially distributed\
            value.
        pval: Output the results as a pure (estimated) p-value.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dNormalityTest",
        "input": input_,
        "prefix": prefix,
        "noexp": noexp,
        "pval": pval,
    }
    return params


def v_3d_normality_test_cargs(
    params: V3dNormalityTestParameters,
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
    cargs.append("3dNormalityTest")
    cargs.append(execution.input_file(params.get("input")))
    cargs.extend([
        "-prefix",
        params.get("prefix")
    ])
    if params.get("noexp"):
        cargs.append("-noexp")
    if params.get("pval"):
        cargs.append("-pval")
    return cargs


def v_3d_normality_test_outputs(
    params: V3dNormalityTestParameters,
    execution: Execution,
) -> V3dNormalityTestOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dNormalityTestOutputs(
        root=execution.output_file("."),
        output_dataset=execution.output_file(params.get("prefix") + "+orig.*"),
    )
    return ret


def v_3d_normality_test_execute(
    params: V3dNormalityTestParameters,
    execution: Execution,
) -> V3dNormalityTestOutputs:
    """
    This program tests the input values at each voxel for normality using the
    Anderson-Darling method.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dNormalityTestOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_normality_test_cargs(params, execution)
    ret = v_3d_normality_test_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_normality_test(
    input_: InputPathType,
    prefix: str,
    noexp: bool = False,
    pval: bool = False,
    runner: Runner | None = None,
) -> V3dNormalityTestOutputs:
    """
    This program tests the input values at each voxel for normality using the
    Anderson-Darling method.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_: Specifies the input dataset.
        prefix: Specifies the name for the output dataset.
        noexp: Do not convert the A-D statistic to an exponentially distributed\
            value.
        pval: Output the results as a pure (estimated) p-value.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dNormalityTestOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_NORMALITY_TEST_METADATA)
    params = v_3d_normality_test_params(
        input_=input_,
        prefix=prefix,
        noexp=noexp,
        pval=pval,
    )
    return v_3d_normality_test_execute(params, execution)


__all__ = [
    "V3dNormalityTestOutputs",
    "V3dNormalityTestParameters",
    "V_3D_NORMALITY_TEST_METADATA",
    "v_3d_normality_test",
    "v_3d_normality_test_params",
]
